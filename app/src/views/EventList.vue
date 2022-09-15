<script setup lang="ts">
import { useEventStore } from '../stores/EventStore'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const eventStore = useEventStore()
const router = useRouter()

onMounted(()=> {
  eventStore.fetchEvents().catch(error => {
    router.push({
      name: 'ErrorDisplay',
      params: { error: error }
    })
  })
})
</script>

<template>
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
