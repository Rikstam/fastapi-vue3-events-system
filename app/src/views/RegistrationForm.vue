<template>
    <form @submit.prevent="submit">
        <BaseInput
            label="First name"
            type="text"
            v-model="first_name"
            :error="errors.first_name"
      />
      <BaseInput
            label="Last name"
            type="text"
            v-model="last_name"
            :error="errors.last_name"
      />
      <BaseInput
            label="Username"
            type="text"
            v-model="username"
            :error="errors.username"
      />
     
      <BaseInput
        label="Email"
        type="email"
        :modelValue="email"
        @change="handleChange"
        :error="errors.email"
      />
  
      <BaseInput
        label="Password"
        type="password"
        v-model="password"
        :error="errors.password"
      />
  
      <BaseButton
        type="submit"
        class="-fill-gradient"
      >
      Submit
      </BaseButton>
    </form>
  </template>
  
<script setup lang="ts">
import { useField, useForm } from 'vee-validate'
import BaseInput from '../components/BaseInput.vue'
import BaseButton from '../components/BaseButton.vue'
import {object, string} from 'yup'
import { useUserStore } from '../stores/UserStore'
import { useRouter } from 'vue-router'

const validationSchema = object({
  email: string().email().required(),
  password: string().required(),
  first_name: string().required(),
  last_name: string().required(),
  username: string().required(),
})
const {setFieldValue, handleSubmit, errors} = useForm({
 validationSchema
})

const router = useRouter()
const userStore = useUserStore()
const handleChange = ((event: Event) => {
    setFieldValue('email', (event.target as HTMLInputElement).value)
})

const submit = handleSubmit((values)=> {
  userStore.registerUser(
  {
    username: username.value,
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    password: password.value
  }
)
  .then(() => {
    router.push({
      name: 'Login',
    })
  })
  .catch(error => {
    router.push({
      name: 'ErrorDisplay',
      params: { error: error }
    })
  })
})
const {value: first_name} = useField<string>('first_name')
const {value: last_name} = useField<string>('last_name')
const {value: username} = useField<string>('username')
const {value: email} = useField<string>('email')
const {value: password} = useField<string>('password')

</script>
  