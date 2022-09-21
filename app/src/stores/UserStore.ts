import { defineStore } from 'pinia'
import { CreateUserPayload, LoginUserPayload, UserInfo } from '../types'
import UserService from '../services/UserService'

export const useUserStore = defineStore('UserStore', {
    state: () => ({
        user: null as UserInfo | null,
        token: null as string | null
    }),
    getters: {
        firstName(): string {
            if (this.user) {
                return this.user.first_name
            }
            return ''
        },
        loggedIn(): boolean {
            return this.token !== null
        }
    },
    actions: {
        registerUser(credentials: CreateUserPayload) {
            return UserService.registerUser(credentials)
                .then((response) => {
                    console.log(response.data)
                })
                .catch(error => {
                    throw error
                })
        },
        login(credentials: LoginUserPayload) {
            return UserService.loginUser(credentials)
                .then((response) => {
                    console.log(response.data)
                    const token = response.data.access_token
                    const userInfo = response.data.userInfo
                    this.user = userInfo
                    this.token = token
                    localStorage.setItem('user', JSON.stringify({ token, userInfo }))
                })
                .catch(error => {
                    throw error
                })
        },
        logout() {
            this.user = null
            this.token = null
            localStorage.removeItem('user')
            location.reload()
        }
    }
})