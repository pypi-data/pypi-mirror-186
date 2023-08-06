from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
from ..req_utils import *
from tqdm import tqdm
from ..metrics.regression import mean_absolute_percentage_error
class models():
    def __init__(self, aR_info,show=None):
        self.aR_info = aR_info
        self.show    = show
        check_period(self.aR_info.period)
        check_S_modelname(self.aR_info.modelname)
        if bool(self.aR_info.metric):
            evaluate(self.aR_info.metric)
    @staticmethod
    def opt(name,params, s,train,test):
        """Function of optimization to obtain the best parameters p,q,d and P,Q,D
           by choosing the parameters that gives the smallest MSE
            Arguments:
            ARIMA
            parameters_list - list with (p, d, q)
            p - autoregression order
            d - integration order
            q - moving average order
           Arguments:
            SARIMA
            parameters_list - list with (p, d, q, P, D, Q)
            p - autoregression order
            d - integration order
            q - moving average order
            P - seasonal autoregression order
            D - seasonal integration order
            Q - seasonal moving average order
            s - length of season
          Return:
            order - List with the optimal values of params(p,d,q,P,D,Q)
        """

        res=[]
        for i in tqdm(range(len(params))):
            par=params[i]
            try:
                if name.lower() == "sarima":
                    model = SARIMAX(train, order=(par[0], par[1], par[2]), seasonal_order=(par[3], par[4], par[5], s)).fit(disp=False)
                else:
                    model = ARIMA(train,order=(par[0], par[1], par[2])).fit()
            except:
                continue
            fcast = model.forecast(len(test),alpha=0.05,dynamic = True)
            mape = mean_absolute_percentage_error(y_true=test,y_pred=fcast)
            res.append([par, mape])
        res_df = pd.DataFrame(res)
        res_df.columns = ['(p,d,q)x(P,D,Q)', 'MAPE']
        #Sort in ascending order, lower ? is better
        res_df = res_df.sort_values(by='MAPE', ascending=True).reset_index(drop=True)
        return res_df

