import pandas as pd
import numpy as np
import statsmodels.api as sm

class single_signal_test(object):
    def __init__(self) -> None:
        pass
    
    def cal_turnover(self,df,ndays):
        # holdings:
        # pd.Series
        # multiindex: timestamp,code
        # 值都是1
        holdings = df.copy()
        holdings = holdings.unstack().dropna(how ='all',axis = 1)
        holdings = holdings.apply(lambda x: x/x.sum(),axis = 1)
        holdings = holdings.fillna(0)
        return (holdings.diff(ndays).abs().sum(axis = 1)/2)
    
    def cal_holdingnums(self,df):
        # holdings:
        # pd.Series
        # multiindex: timestamp,code
        # 值都是1
        holdings = df.copy()
        holdings = holdings.groupby(level = 0).sum()
        return holdings

    def one_factor_grouper(self,df,factorname,quantiles): # 分组
        # concatdf:pd.DataFrame
        # factorname: str
        # multiindex: timestamp,code
        # columns: nday_return, factorname1, factorname2...
        concatdf = df[[factorname]].copy()
        concatdf[factorname+'_rank'] = concatdf[factorname].groupby(level = 'date').rank()
        concatdf[factorname+'_quantile'] =concatdf[factorname+'_rank'].dropna().groupby(level = 'date').apply(lambda x: (x//round(x.max()/quantiles))+1)
        over_quantile = concatdf[(concatdf[factorname+'_quantile']>quantiles)].index
        concatdf.loc[over_quantile,factorname+'_quantile'] = quantiles
        return concatdf

    def one_factor_return(self,df,factorname,ndays,return_col): # 计算分组收益
        qreturn = df.groupby(level = 'date').apply(lambda x: x.groupby(factorname+'_quantile')[[return_col]].mean()/ndays).unstack()
        qreturn.columns = [i[1] for i in list(qreturn)]
        return qreturn
    
    def one_factor_icir(self,df,factorname,return_col):
        ic = df.groupby(level = 'date').apply(lambda x: x[[return_col,factorname]].corr('spearman'))
        ic_org = ic[ic.index.get_level_values(1) ==return_col][factorname].dropna()
        return ic_org

    def one_factor_ret_sharp(self,qreturn,ret_freq):
        return qreturn.mean()/qreturn.std()*np.sqrt(252/ret_freq)

class multi_factor_test(object):
    def __init__(self) -> None:
        pass

    def multif_corr_ana(self,df,factornamelist): # 多因子相关性分析
        # df:pd.DataFrame
        # factornamelist: strlist
        # multiindex: timestamp,code
        # columns: nday_return, factorname1, factorname2...
        df_ana = df[factornamelist].groupby(level = 'date').corr()
        corr_mean = df_ana.groupby(level = 1).mean() # corr之后的矩阵第二层没名字，所以用1来表示；第二层是因子名
        corr_ir = df_ana.groupby(level = 1).mean()/df_ana.groupby(level = 1).std()  
        return corr_mean.loc[list(corr_mean)],corr_ir.loc[list(corr_ir)]

    def multif_pca_ana(self,originalFactor,domain_factor_nums): # 多因子pca分析
        # originalFactor: pd.DataFrame
        # multiindex: timestamp,code
        # columns: factorname1, factorname2...
        from sklearn import preprocessing
        data = originalFactor.groupby(level = 'date').apply(lambda x: preprocessing.scale(x))
        data = np.vstack(data.values)
        from sklearn.decomposition import PCA
        pcaModel = PCA(domain_factor_nums)
        pcaModel.fit(data)
        pcaFactors = pcaModel.transform(data)
        pcaFactors = pd.DataFrame(pcaFactors)
        pcaFactors.index = originalFactor.index
        pcaFactors.columns = ['pca_'+str(i) for i in range(domain_factor_nums)]
        return pcaModel.explained_variance_,pcaModel.explained_variance_ratio_,pcaFactors
    
    def multif_tsstable_test(self,originalData):
        # originalFactor: pd.DataFrame
        # multiindex: timestamp,code
        # columns: factorname1, factorname2...
        from statsmodels.tsa.stattools import adfuller
        data = originalData.copy()#.groupby(level = 0).apply(lambda x: (x-x.mean())/x.std())不要再标准化了！！
        mean_pvalue = data.groupby(level = 'date').apply(lambda x:x.mean()).apply(lambda x: adfuller(x)[1])
        std_pvalue = data.groupby(level = 'date').apply(lambda x:x.std()).apply(lambda x: adfuller(x)[1])
        skew_pvalue = data.groupby(level = 'date').apply(lambda x:x.skew()).apply(lambda x: adfuller(x)[1])
        kurt_pvalue = data.groupby(level = 'date').apply(lambda x:x.kurt()).apply(lambda x: adfuller(x)[1])
        yarn_pvalue = pd.concat([mean_pvalue,std_pvalue,skew_pvalue,kurt_pvalue],axis = 1)
        yarn_pvalue.columns = ['mean','std','skew','kurt']
        return yarn_pvalue
    
    def multif_cal_weight(self,factordf,factorlist,return_col,weight_type:str):
        # factordf: pd.DataFrame
        # multiindex: timestamp,code
        # columns: factorname1, factorname2...,returndata
        # factorlist: strlist
        # return_col: column name, str
        df = factordf.copy()
        weight = df.groupby(level = 'date').apply(lambda x: sm.formula.ols(return_col+'~'+'+'.join(factorlist),data = x).fit().params)
        if weight_type == '因子收益信息比加权':
            return weight.mean()/weight.std()
        # if weight_type == '风险平价加权':
        #     cov = weight[factorlist].cov()
        #     from scipy.optimize import minimize
        #     def objective(x):
        #         w_cov = np.dot(cov,x.T)
        #         for n in range(len(x)):
        #             w_cov[n] *= x[n]
        #         mat = np.array([w_cov]*len(x))
        #         scale = 1/sum(abs(mat))
        #         return np.sum(abs(scale*(mat-mat.T)))
        #     initial_w=np.array([0.2]*len(factorlist))
        #     cons = []
        #     cons.append({'type':'eq','fun':lambda x: sum(x)-1})
        #     for i in range(len(initial_w)):
        #         cons.append({'type':'ineq','fun':lambda x: x[i]})
        #     #结果
        #     res=minimize(objective,initial_w,method='SLSQP',constraints=cons)
        #     params = pd.Series(res.x)
        #     params.index = cov.index
        #     return params

    def weighted_factor(self,factordf,weight):
        # factordf: pd.DataFrame
        # multiindex: timestamp,code
        # columns: factorname1, factorname2...
        # weight:pd.Series
        wf = (weight*factordf).sum(axis = 1)

        return pd.DataFrame(wf,columns = ['weighted_factor'])
        
    def del_updown_limit(self,factordf,daybar):
        # 剔除涨跌停
        notuplimit = daybar[~(daybar.close == daybar.limit_up)]
        notdownlimit = daybar[~(daybar.close == daybar.limit_down)]
        factordf = factordf[factordf.index.isin(notuplimit.index)]
        factordf = factordf[factordf.index.isin(notdownlimit.index)]
        return factordf

    def in_some_pool(self,factordf,pool_components):
        factordf['inpool']=pool_components.applymap(lambda x:1)
        factordf['inpool'] = factordf['inpool'].apply(lambda x: 1 if x>0 else 0)
        testdf = factordf[factordf['inpool']>=1]
        return testdf
    
    def orthog(self,factor_mat, y, xlist):
        df = factor_mat.copy()
        regre = sm.formula.ols(y+'~'+'+'.join(xlist),data = df).fit()
        params = regre.params[~(regre.params.index == 'Intercept')]
        intercept = regre.params[(regre.params.index == 'Intercept')]
        residual = df[y] - (df[list(params.index)]*params).sum(axis = 1) - intercept.values
        residual = pd.DataFrame(residual)
        residual.columns = [y]
        return residual,params
    
    def mat_orthog(self,factor_mat):
        temp1 = factor_mat.copy()
        for i in list(temp1):
            fclist = list(filter(lambda x: x!=i,list(temp1)))
            temp1[i] = self.orthog(temp1,i,fclist)[0]
        return temp1

class Barra_factor_ana(object):
    '''
    1. growth要求至少504天的数据，部分股票不满足该条件会导致在因子整合到一起的时候被剔除
    2. barrafactor必须为双重索引，且第一重索引是日期，第二重索引是标的
    '''
    def __init__(self,df=None,start_date=None,end_date=None,dir=None,skip_fileload=None) -> None:
        # 预加载数据
        if not skip_fileload:
            self.price = df
            dailyreturn = df/df.shift(1)-1
            dailyreturn.dropna(how = 'all',inplace=True)
            self.returndata = dailyreturn
            self.start_date = start_date
            self.end_date = end_date
            import os
            filelist = os.listdir(dir)
            self.filedict = {}
            for f in filelist:
                if f[-3:]=='csv':
                    self.filedict[f[:-4]] = pd.read_csv(dir+f,index_col = [0,1])
            pass

    def rise_barra_factors(self,rank_normalize:bool):
        print('rise size')
        self.size = np.log(self.filedict['market_cap']).dropna()
        def OLSparams(y,x):
            print('rise beta')
            X_ = x.droplevel('order_book_id')
            df = y.copy()
            df['market_r'] = X_['r']
            dflist = list(df.rolling(100))[100:]
            paramslist = []
            for olsdf in dflist:
                mod = sm.OLS(olsdf,sm.add_constant(olsdf['market_r']))
                re = mod.fit()
                params = re.params.T
                params.index = olsdf.columns
                params = params[params.index!='market_r']
                params['date'] = olsdf.index[-1]
                params = params.rename(columns = {'market_r':'beta'})
                paramslist.append(params)
            olsparams = pd.concat(paramslist).set_index('date',append=True).unstack().T
            constdf = olsparams.loc['const'].ewm(halflife = 63,ignore_na = True,adjust = False).mean().stack()
            betadf = olsparams.loc['beta'].ewm(halflife = 63,ignore_na = True,adjust = False).mean().stack()
            # cal residual
            mkt_df = pd.concat([X_['r']]*len(list(betadf.unstack())),axis = 1)
            mkt_df.columns = list(betadf.unstack())
            residual = y - betadf.unstack()*mkt_df - constdf.unstack() # 这里的residual已经是经过ewm的beta和const计算得到的就不用再ewm了
            return {'beta':betadf,'const':constdf,'residual':residual}
        def MOMTM(y):
            print('rise momentum')
            df = np.log(1+y)
            momtm = df.ewm(halflife=126,ignore_na = True,adjust = False).mean().stack()
            momtm = pd.DataFrame(momtm)
            momtm.columns = ['momentum']
            return momtm
        def CMRA(y,T):
            date = y.index[-1]
            dflist= []
            for i in range(1,T+1):
                pct_n_month = pd.DataFrame((y/y.shift(21*i)-1).iloc[-1])
                dflist.append(pct_n_month)
            df = pd.concat(dflist,axis =1)
            zmax = df.max(axis =1)
            zmin = df.min(axis = 1)
            cmra = pd.DataFrame(zmax-zmin,columns = [date]).T
            return cmra
        def orthog(barrafactor,y,xlist):
            df = barrafactor.copy()
            regre = sm.formula.ols(y+'~'+'+'.join(xlist),data = df).fit()
            for p in xlist:
                df[p]*= regre.params[p]
            df[y+'_orth'] = df[y] - df[xlist].sum(axis = 1)-regre.params['Intercept']
            return df[[y+'_orth']]

        # beta
        self.olsparams = OLSparams(self.returndata,self.filedict['market_r'])
        self.beta = pd.DataFrame(self.olsparams['beta']).dropna()
        self.beta.columns = ['beta']

        # momentum
        self.momtm = MOMTM(self.returndata).dropna()
        
        # residual volatility
        print('rise residual volatility')
        self.hist_volatility = self.returndata.ewm(halflife = 42,ignore_na = True,adjust = False).std().dropna(how = 'all')
        CMRAlist = list(self.price.rolling(252))[252:]
        self.CMRA = pd.concat(list(map(lambda x: CMRA(x,12),CMRAlist)))
        self.Hsigma = self.olsparams['residual']
        self.residual_volatility = pd.DataFrame((self.hist_volatility*0.74+self.CMRA*0.16+self.Hsigma*0.1).stack()).dropna()
        self.residual_volatility.columns = ['residual_volatility']

        # non-linear size
        print('rise non-linear size')
        self.nlsize = (self.size**3).dropna()
        self.nlsize.columns = ['nlsize']

        # Bp
        print('rise Bp')
        self.Bp = self.filedict['Bp'].dropna()
        
        # liquidity
        print('rise Liquidity')
        self.tvrdf = self.filedict['turnover']
        self.liq_1m = self.tvrdf.groupby(level = 1).apply(lambda x: x.sort_index().rolling(22).mean())
        self.liq_3m = self.tvrdf.groupby(level = 1).apply(lambda x: x.sort_index().rolling(74).mean())
        self.liq_12m = self.tvrdf.groupby(level = 1).apply(lambda x: x.sort_index().rolling(252).mean())
        self.liq = (0.35*self.liq_1m + 0.35*self.liq_3m + 0.3*self.liq_12m).dropna()

        print('rise Earning Yield')
        self.earning_yield = pd.concat([self.filedict['Ep'],self.filedict['Sp']],axis = 1)
        self.earning_yield['earning_yield'] = self.earning_yield['ep_ratio_ttm']*0.66+self.earning_yield['sp_ratio_ttm']*0.34
        self.earning_yield = self.earning_yield[['earning_yield']].dropna()
        
        # growth
        print('rise growth')
        NP = self.filedict['NPGO'].unstack()
        NP = (NP-NP.shift(504))/NP.shift(504).abs()
        NP = NP.stack()
        RVN = self.filedict['RGO'].unstack()
        RVN = (RVN - RVN.shift(504))/RVN.shift(504).abs()
        RVN = RVN.stack()
        self.growth = pd.DataFrame(NP['net_profit_parent_company_ttm_0']*0.34+RVN['revenue_ttm_0']*0.66)
        self.growth.columns = ['growth']
        self.growth.dropna(inplace=True)

        # leverage
        print('rise leverage')
        self.leverage = pd.concat([self.filedict['MLEV'],self.filedict['DTOA'],self.filedict['BLEV']],axis = 1)
        self.leverage['leverage'] = self.leverage['du_equity_multiplier_ttm']*0.38+self.leverage['debt_to_asset_ratio_ttm']*0.35+self.leverage['book_leverage_ttm']*0.27
        self.leverage = self.leverage[['leverage']].dropna()

        # concat
        self.barrafactor = pd.concat([
                                    self.size,
                                    self.beta,
                                    self.momtm,
                                    self.residual_volatility,
                                    self.nlsize,
                                    self.Bp,
                                    self.liq,
                                    self.earning_yield,
                                    self.growth,
                                    self.leverage],axis = 1).sort_index(level = 0)
        '''正则化'''
        # 未经正则化的原始因子已存为类变量，可直接调用
        print('Orthogonalizing....')
        y = ['residual_volatility','nlsize','turnover']
        xlist = ['circulation_A','beta']   
        # 不dropna会报错
        self.barrafactor['residual_volatility'] = self.barrafactor.dropna().groupby(level = 0).apply(lambda x: orthog(x,y[0],xlist))
        self.barrafactor['nlsize'] = self.barrafactor.dropna().groupby(level = 0).apply(lambda x: orthog(x,y[1],xlist[:1]))
        self.barrafactor['turnover'] = self.barrafactor.dropna().groupby(level = 0).apply(lambda x: orthog(x,y[2],xlist[:1]))
        # rank标准化
        if rank_normalize:
            self.barrafactor = self.barrafactor.groupby(level = 0).apply(lambda x: x.rank())

    def barra_compose(self,factordata):
        # 因子是rank数据
        decompose = pd.concat([self.barrafactor,factordata],axis = 1).dropna().rename_axis(['date','symbol'])
        def orthog(barrafactor,y,xlist):
            df = barrafactor.copy()
            regre = sm.formula.ols(y+'~'+'+'.join(xlist),data = df).fit()
            params = regre.params[~(regre.params.index == 'Intercept')]
            intercept = regre.params[(regre.params.index == 'Intercept')]
            residual = df[y] - (df[list(params.index)]*params).sum(axis = 1) - intercept.values
            return residual,params
        # 这种方法只算一天的会错
        # residual_ols =decompose.groupby(level = 0).apply(lambda x: orthog(x,list(decompose)[-1],list(decompose)[:-1])[0]).droplevel(0)
        # params_ols =decompose.groupby(level = 0).apply(lambda x: orthog(x,list(decompose)[-1],list(decompose)[:-1])[1])
        # return residual_ols,params_ols
        decomposebyday = list(decompose.groupby(level = 'date'))
        residual_olslist = []
        params_olslist = []
        for df in decomposebyday:
            x = df[1]
            residual_ols,params_ols = orthog(x,list(decompose)[-1],list(decompose)[:-1])
            residual_olslist.append(residual_ols)
            params_olslist.append(pd.DataFrame(params_ols,columns = [df[0]]).T)
        return pd.concat(residual_olslist),pd.concat(params_olslist)

    def barra_style_pool(self,style):
        bystyle = self.barrafactor[[style]]
        bystyle[style+'_group'] = bystyle[style].dropna().groupby(level = 0).apply(lambda x: (x//round(x.max()/10))+1)
        return bystyle

    def factor_performance_bystyle(self,factordata,factorname,style):
        # 即便因子在风格上没有偏斜，仍然会有不同风格上因子表现不同的情况
        bystyle = pd.concat([factordata,self.barrafactor[[style]]],axis = 1)
        bystyle[style+'_group'] = bystyle[style].dropna().groupby(level = 0).apply(lambda x: (x//round(x.max()/10))+1)
        over_quantile = bystyle[(bystyle[style+'_group']>10)].index
        bystyle.loc[over_quantile,style+'_group'] = 10
        ic_daily = bystyle.groupby(style+'_group').apply(lambda x: x[[factorname,'nday_return']].groupby(level = 0).apply(lambda x: x.corr('spearman').iloc[0,1])).T
        return ic_daily.mean()/ic_daily.std()

class plot_tools(object):
    def __init__(self) -> None:
        pass

    def trio_plt(self,qmean,qcum,quantiles): # 画收益图
        import matplotlib.pyplot as plt
        qmean[list(range(1,quantiles+1))].plot(kind= 'bar',title = 'mean')
        plt.show()
        qcum[list(range(1,quantiles+1))].plot(title = 'cumreturn')
        plt.legend(loc = 'upper center',bbox_to_anchor=(1.1, 1.02))
        plt.show()
        (qcum[10]-qcum[1]).plot(title = 'long-short')
        plt.show()

    def fbplot(self,frontplot,bgplot,c,fname,bname):
        # frontplot,bgplot:
        # pd.Series
        # multiindex: timestamp,code
        import matplotlib.pyplot as plt
        import matplotlib.ticker as ticker
        tickspace = len(frontplot)//12
        fig = plt.figure()
        a1=fig.add_axes([0,0,1,1])
        a1.bar(frontplot.index,bgplot.loc[frontplot.index],color = c)
        a1.tick_params(axis='x', labelrotation= 30)
        a1.xaxis.set_major_locator(ticker.MultipleLocator(tickspace))

        a2 = a1.twinx()
        a2.plot(frontplot.index,frontplot,color = 'red')
        a2.tick_params(axis='x', labelrotation= 30)
        a2.xaxis.set_major_locator(ticker.MultipleLocator(tickspace))
        

        fig.legend(frameon = False,labels = [bname+'(left)',fname+'(right)'],loc = 'upper center')
        plt.show()

class mate_alphalens(object):
    def __init__(self) -> None:
        pass

    def index_mate(self,factordata,price):
        fcdf = factordata.reset_index()
        fcdf['date'] = pd.to_datetime(fcdf['date'])
        fcdf = fcdf.rename(columns = {'symbol':'asset'}).set_index(['date','asset'])
        ptemp = price.copy()
        ptemp.index = pd.to_datetime(ptemp.index)
        return fcdf,ptemp
    
    def trans_ex_return(self,clean_factor,index_price):
        from alphalens import utils
        index_price['factor'] = 1
        base_ret = utils.compute_forward_returns(index_price[['factor']],index_price['close'].unstack())
        base_ret = base_ret.droplevel('asset').reindex(clean_factor.index.get_level_values(0))
        base_ret['asset'] = clean_factor.index.get_level_values('asset')
        base_ret = base_ret.set_index(['asset'],append=True)
        df = clean_factor.copy()
        df[list(base_ret)]-= base_ret
        return df