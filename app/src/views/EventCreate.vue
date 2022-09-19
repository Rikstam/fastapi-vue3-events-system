<script setup lang="ts">
import { useEventStore } from '../stores/EventStore'
import { useUserStore } from '../stores/UserStore'
import { useRouter } from 'vue-router'
import BaseInput from '../components/BaseInput.vue'
import BaseSelect from '../components/BaseSelect.vue'
import BaseCheckbox from '../components/BaseCheckbox.vue'
import BaseRadioGroup from '../components/BaseRadioGroup.vue'
import { useField, useForm } from 'vee-validate'

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
const required = (value: string | number) => {
      const requiredMessage = 'This field is required'
      if (value === undefined || value === null) return requiredMessage
      if (!String(value).length) return requiredMessage
      return true
    }
const minLength = (number: number, value: string | number) => {
  if (String(value).length < number) return 'Please type at least ' + number + ' characters'
  return true
}

const anything = () => {
  return true
}

const validationSchema = {
  category: required,
  title: (value: string) => {
    const req = required(value)
    if (req !== true) return req
    
    const min = minLength(3, value)
    if (min !== true ) return min

    return true
  },
  description: required,
  location: required,
  date: required,
  time: required,
  organization: required,
  catering: anything,
  music: anything,
  pets: anything
}

const { handleSubmit, errors } = useForm({
  validationSchema,
  initialValues: {
    category: '',
    title: '',
    description: '',
    location: '',
    organization: '',
    pets: 1,
    catering: false,
    music: false,
    date: '',
    time: ''
  }
})

const submit = handleSubmit((values) => {
  eventStore.createEvent(
  {
    category: category.value,
    title: title.value,
    description: description.value,
    location: location.value,
    date: date.value,
    time: time.value,
    organization: organization.value,
    pets: pets.value,
    catering: catering.value,
    music: music.value
  }
)
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
})

const { value: category } = useField<string>('category')
const { value: title } = useField<string>('title')
const { value: description } = useField<string>('description')
const { value: location} = useField<string>('location')
const { value: date } = useField<string>('date')
const { value: time } = useField<string>('time')
const { value: organization } = useField<string>('organization')
const { value: pets } = useField<number>('pets')
const { value: catering } = useField<boolean>('catering')
const { value: music } = useField<boolean>('music')

const userStore = useUserStore()
const eventStore = useEventStore()

const onSubmit = () => {
}
</script>

<template>
  <h1>Create an event</h1>

  <div class="form-container">
    <form @submit.prevent="submit">
      <BaseSelect  
        v-model="category"
        :options="categories"
        :error="errors.category"
        label="Select a category:"
        />
      <fieldset>
          <legend>Name & describe your event</legend>
          <BaseInput
            v-model="title"
            :error="errors.title"
            label="Title"
            type="text"
      />
        <BaseInput
          v-model="description"
          :error="errors.description"
          label="Description"
          type="text"
        />
      </fieldset>
     
      
      <fieldset>
        <legend>Where is your event?</legend>
        <BaseInput 
        v-model="location"
        :error="errors.location"
        label="Location"
        type="text"
      />
      </fieldset>

      <fieldset>
        <legend>Organization</legend>
        <BaseInput 
        v-model="organization"
        :error="errors.organization"
        label="Organization"
        type="text"
      />
      </fieldset>
     
     <fieldset>
      <legend>Pets</legend>
      <p>Are pets allowed?</p>
        <BaseRadioGroup 
          v-model="pets"
          :error="errors.pets"
          name="pets"
          :options="petOptions"
          vertical/>
     </fieldset>
     <fieldset>
      <legend>Extras</legend>
      <div>
        <BaseCheckbox
          v-model="catering"
          :error="errors.catering"
          label="Catering"/>
      </div>
      <div>
        <BaseCheckbox
          v-model="music"
          :error="errors.music"
          label="Live music"/>
      </div>
    </fieldset>
    <fieldset>
      <legend>When is your event?</legend>
      <BaseInput
        v-model="date"
        type="date"
        label="Date"
        :error="errors.date"/>
      <BaseInput
        v-model="time"
        type="time"
        label="Time"
        :error="errors.time"/>
    </fieldset>
    <button type="submit">Submit</button>
    </form>
  </div>
</template>
<style>
  fieldset {
    border: 0px;
    margin: 0px;
    padding: 0px;
  }
  legend {
    font-size: 28px;
    font-weight: 700;
    margin-top: 20px;
  }
</style>