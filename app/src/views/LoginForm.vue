<template>
    <form @submit.prevent="submit">
      <BaseInput
        label="Email"
        type="email"
        :error="errors.email"
        :modelValue="email"
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
})
const {handleSubmit, errors} = useForm({
 validationSchema
})

const router = useRouter()

const submit = handleSubmit((values)=> {
  console.log(values)
  router.push({
      name: 'EventList',
    })
})
const {value: email, handleChange} = useField<string>('email')
const {value: password} = useField<string>('password')

</script>
  