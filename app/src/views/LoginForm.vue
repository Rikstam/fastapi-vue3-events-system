<template>
    <form @submit.prevent="submit">
      <BaseInput
        label="Username"
        type="text"
        :error="errors.username"
        :modelValue="username"
        @change="handleChange"
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
    <p v-if="loginError">{{ loginError}}</p>
    <router-link to="/sign-up">
      Don't have an account? Register.
    </router-link>
  </template>
  
<script setup lang="ts">
import { useField, useForm } from 'vee-validate'
import BaseInput from '../components/BaseInput.vue'
import BaseButton from '../components/BaseButton.vue'
import {object, string} from 'yup'
import { useUserStore } from '../stores/UserStore'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const validationSchema = object({
  username: string().required(),
  password: string().required(),
})
const {handleSubmit, errors} = useForm({
 validationSchema
})

const loginError = ref('')

const router = useRouter()
const userStore = useUserStore()
const submit = handleSubmit((values) => {
  userStore.login({
    username: username.value,
    password: password.value
  })
  .then(() => {
    router.push({
      name: 'Dashboard',
    })
  })
  .catch((error) => {
    console.log(error.response)
    loginError.value = error.response.data.detail
  })
})
const {value: username, handleChange} = useField<string>('username')
const {value: password} = useField<string>('password')

</script>
  