<template>
    <div id="nav">
      <router-link :to="{ name: 'EventList' }">Events</router-link> |
      <router-link :to="{ name: 'About' }">About</router-link> | 
      <router-link v-if="!userStore.user" :to="{ name: 'Login' }">Login</router-link> | 
      <router-link v-if="!userStore.user" :to="{ name: 'Signup' }">Sign up</router-link>
      |
      <router-link :to="{ name: 'EventCreate' }">Create Event</router-link> | 
      <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
      <p v-if="userStore.user">Logged in as USER: {{userStore.user.username}}</p>
    </div>
</template>

<script setup lang="ts">
    import { useUserStore } from '../stores/UserStore';
    const userStore = useUserStore()
</script>