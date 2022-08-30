<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useEventStore } from '../stores/EventStore'
import { useUserStore } from '../stores/UserStore'
import { EventItem } from '../types'
import { useRouter, useRoute } from 'vue-router'

export default defineComponent({
  setup() {
    const router = useRouter()
    const categories = [
        'sustainability',
        'nature',
        'animal welfare',
        'housing',
        'education',
        'food',
        'community'
     ]
     const eventData = {
        category: '',
        title: '',
        description: '',
        location: '',
        date: '',
        time: '',
        organization: ''
      } as EventItem

     const userStore = useUserStore()
     const eventStore = useEventStore()

     const onSubmit = () => {
      const event = {
        ...eventData,
        organization: userStore.user
      }
      eventStore.createEvent(event)
        .then(() => {
          router.push({
            name: 'EventDetails',
            params: { id: event.id }
          })
        })
        .catch(error => {
          router.push({
            name: 'ErrorDisplay',
            params: { error: error }
          })
        })
     }
     return {
      eventStore,
      userStore,
      categories,
      event: ref(eventData),
      onSubmit
     }
  },
  methods: {
    
  }
})
</script>

<template>
  <h1>Create an event</h1>

  <div class="form-container">
    <form @submit.prevent="onSubmit">
      <label>Select a category: </label>
      <select v-model="event.category">
        <option
          v-for="option in categories"
          :value="option"
          :key="option"
          :selected="option === event.category"
        >
          {{ option }}
        </option>
      </select>

      <h3>Name & describe your event</h3>

      <label>Title</label>
      <input v-model="event.title" type="text" placeholder="Title" />

      <label>Description</label>
      <input
        v-model="event.description"
        type="text"
        placeholder="Description"
      />

      <h3>Where is your event?</h3>

      <label>Location</label>
      <input v-model="event.location" type="text" placeholder="Location" />

      <h3>When is your event?</h3>
      <label>Date</label>
      <input v-model="event.date" type="text" placeholder="Date" />

      <label>Time</label>
      <input v-model="event.time" type="text" placeholder="Time" />

      <button type="submit">Submit</button>
    </form>
  </div>
</template>
