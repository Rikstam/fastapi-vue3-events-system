<script setup lang="ts">
import { reactive } from 'vue'
import { useEventStore } from '../stores/EventStore'
import { useUserStore } from '../stores/UserStore'
import { EventItem } from '../types'
import { useRouter } from 'vue-router'
import BaseInput from '../components/BaseInput.vue'
import BaseSelect from '../components/BaseSelect.vue'
import BaseCheckbox from '../components/BaseCheckbox.vue'
import BaseRadioGroup from '../components/BaseRadioGroup.vue'

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

const petOptions = [
  {label: 'Yes', value: 1},
  {label: 'No', value: 0}
]

const event = reactive<EventItem>({
  category: '',
  title: '',
  description: '',
  location: '',
  date: '',
  time: '',
  organization: '',
  catering: false,
  music: false,
  pets: 0
})

const userStore = useUserStore()
const eventStore = useEventStore()

const onSubmit = () => {
eventStore.createEvent(event)
  .then(() => {
    router.push({
      name: 'EventList',
    })
  })
  .catch(error => {
    router.push({
      name: 'ErrorDisplay',
      params: { error: error }
    })
  })
}
</script>

<template>
  <h1>Create an event</h1>

  <div class="form-container">
    <form @submit.prevent="onSubmit">
      <BaseSelect  
        v-model="event.category"
        :options="categories"
        label="Select a category:"
        />
      <h3>Name & describe your event</h3>
      <BaseInput
        v-model="event.title"
        label="Title"
        type="text"
      />
      <BaseInput
        v-model="event.description"
        label="Description"
        type="text"

      />

      <h3>Where is your event?</h3>
      <BaseInput 
        v-model="event.location"
        label="Location"
        type="text"
      />
      <h3>Are pets allowed?</h3>
      <div>
        <BaseRadioGroup 
          v-model="event.pets"
          name="pets"
          :options="petOptions"
          vertical/>
      </div>
      <h3>Extras</h3>
      <div>
        <BaseCheckbox
          v-model="event.catering"
          label="Catering"/>
      </div>

      <div>
        <BaseCheckbox
          v-model="event.music"
          label="Live music"/>
      </div>

      <h3>When is your event?</h3>
      <BaseInput v-model="event.date" type="date" label="Date"/>
      <BaseInput v-model="event.time" type="time" label="Time"/>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>
