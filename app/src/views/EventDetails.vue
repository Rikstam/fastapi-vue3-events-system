<script setup lang="ts">
import { useEventStore } from '../stores/EventStore'
import { computed, defineProps, onMounted } from 'vue'
import { useRouter } from 'vue-router'


const props = defineProps<{id: string}>()
const router = useRouter()
const eventStore = useEventStore()
const event = computed(() => {
  return eventStore.event
})
   
onMounted (() => {
    eventStore.fetchEvent(Number(props.id)).catch(error => {
      router.push({
        name: 'ErrorDisplay',
        params: { error: error }
      })
    })
})
</script>

<template>
  <div v-if="event">
    <h1>{{ event.title }}</h1>
    <p>{{ event.time }} on {{ event.date }} @ {{ event.location }}</p>
    <p>{{ event.description }}</p>
  </div>
</template>
