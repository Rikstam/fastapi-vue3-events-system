import { AxiosError, AxiosInstance, AxiosRequestConfig, AxiosResponse } from "axios"
import { useUserStore } from '../stores/UserStore'


const onRequest = (config: AxiosRequestConfig): AxiosRequestConfig => {
    const userStore = useUserStore()
    if (userStore.loggedIn) {
        config.headers.Authorization = `Bearer ${userStore.token}`
    }
    console.info(`[request] [${JSON.stringify(config)}]`);
    return config;
}

const onRequestError = (error: AxiosError): Promise<AxiosError> => {
    console.error(`[request error] [${JSON.stringify(error)}]`);
    return Promise.reject(error);
}

const onResponse = (response: AxiosResponse): AxiosResponse => {
    console.info(`[response] [${JSON.stringify(response)}]`);
    return response;
}

const onResponseError = (error: AxiosError): Promise<AxiosError> => {
    console.error(`[response error] [${JSON.stringify(error)}]`);
    return Promise.reject(error);
}


export function setupInterceptorsTo(axiosInstance: AxiosInstance): AxiosInstance {
    axiosInstance.interceptors.request.use(onRequest, onRequestError);
    axiosInstance.interceptors.response.use(onResponse, onResponseError);
    return axiosInstance;
}