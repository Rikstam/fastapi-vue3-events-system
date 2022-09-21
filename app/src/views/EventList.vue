<script setup lang="ts">
import { useEventStore } from '../stores/EventStore'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'

import EventCard from '../components/EventCard.vue';

const eventStore = useEventStore()
const router = useRouter()
const isLoading = ref(false)

onBeforeMount(async ()=> {
  isLoading.value = true
  try {
    eventStore.fetchEvents()
  } catch(error) {
    router.push({
      name: 'ErrorDisplay',
      params: { error: `${error}` }
    })
  }
  isLoading.value = false
})
</script>

<template>
  <template v-if="isLoading">
    <p>Loading events</p>
  </template>
  <h1>{{ eventStore.numberOfEvents }} Events for Good</h1>
  <div class="events">
    <EventCard v-for="event in eventStore.events" :key="event.id" :event="event" />
  </div>
</template>

<style scoped>
.events {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
