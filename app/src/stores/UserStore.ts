import { defineStore } from 'pinia'
import { UserItem } from '../types'

export type UserState = {
    user: string
}

export const useUserStore = defineStore('UserStore', {
    state: () => ({
        user: 'Jaffa Pena'
    } as UserState),
    getters: {
        firstName(): string {
            return this.user.split(' ')[0]
        }
    }
})