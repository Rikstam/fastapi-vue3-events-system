import { defineStore } from 'pinia'
import { CreateUserPayload, LoginUserPayload, UserInfo } from '../types'
import UserService from '../services/UserService'

type token = string | null

let token: token = null
let userInfo: UserInfo | null = null


try {
    const initialAuthState: { token: token, userInfo: UserInfo } | null = JSON.parse(localStorage.getItem('user'));

    if (initialAuthState !== null) {
        token = initialAuthState.token
        userInfo = initialAuthState.userInfo
    }
} catch (error) {
    console.log("malformed token data, removing")
    localStorage.removeItem('user')
}

export const useUserStore = defineStore('UserStore', {
    state: () => ({
        user: userInfo as UserInfo | null,
        token: token as token
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