<template>
    <div id="nav">
      <router-link :to="{ name: 'EventList' }">Events</router-link> |
      <router-link :to="{ name: 'About' }">About</router-link> | 
      <template v-if="!userStore.loggedIn">
        <router-link :to="{ name: 'Login' }">Login</router-link> | 
        <router-link :to="{ name: 'Signup' }">Sign up</router-link>|
      </template>
      <template v-if="userStore.loggedIn">
        <router-link  :to="{ name: 'EventCreate' }">Create Event</router-link> | 
      <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
        <p >Logged in as USER: {{ userStore.user?.username }}</p>
      </template>
      <button v-if="userStore.loggedIn" @click="logout">Log out</button>
    </div>
</template>

<script setup lang="ts">
    import { useUserStore } from '../stores/UserStore';
    const userStore = useUserStore()
    const logout = () => {
        userStore.logout()
    }
</script>