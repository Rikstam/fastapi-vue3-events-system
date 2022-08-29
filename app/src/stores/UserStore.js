import { defineStore } from 'pinia'

export const useUserStore = defineStore('UserStore', {
    state: () => ({
           user: 'Jaffa Pena'
        }),
        getters: {
            firstName() {
                return this.user.split(' ')[0]
            }
        }
})