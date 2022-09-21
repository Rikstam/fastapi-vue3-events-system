import axios from 'axios'
import { CreateUserPayload, CreateUserResponse, LoginUserPayload, LoginResponse } from '../types.js'

import { setupInterceptorsTo } from "../plugins/interceptors"

const baseURL = 'http://localhost:8002'

const apiClient = setupInterceptorsTo(axios.create({
    baseURL,
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
}))

const authClient = axios.create({
    baseURL,
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'multipart/form-data'
    }
})

export default {
    registerUser(user: CreateUserPayload) {
        return apiClient.post<CreateUserResponse>('/users', user)
    },
    loginUser(user: LoginUserPayload) {
        const formData = new FormData()
        formData.append('username', user.username)
        formData.append('password', user.password)
        return authClient.post<LoginResponse>('/users/token', formData)
    },
    getAuthUser() {
        return authClient.get<LoginResponse>('/users/me')
    }
}
