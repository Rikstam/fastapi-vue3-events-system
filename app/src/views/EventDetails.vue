<script lang="ts">
import { useEventStore } from '../stores/EventStore'
import { defineComponent, computed } from 'vue'
import { EventItem } from '../types'

export default defineComponent({
  props: ['id'],
  setup() {
    const eventStore = useEventStore()
    const event = computed(() => {
      return eventStore.event
    })
    return {
      eventStore,
      event
    }
  },
  created() {
    this.eventStore.fetchEvent(Number(this.id)).catch(error => {
      this.$router.push({
        name: 'ErrorDisplay',
        params: { error: error }
      })
    })
  }
})
</script>

<template>
  <div v-if="event">
    <h1>{{ event.title }}</h1>
    <p>{{ event.time }} on {{ event.date }} @ {{ event.location }}</p>
    <p>{{ event.description }}</p>
  </div>
</template>
