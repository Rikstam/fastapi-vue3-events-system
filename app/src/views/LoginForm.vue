<template>
    <form @submit.prevent="submit">
      <BaseInput
        label="Email"
        type="email"
        v-model="email"
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

const validationSchema = object({
  email: string().email().required(),
  password: string().email().required(),
})
const {handleSubmit, errors} = useForm({
 validationSchema
})

const submit = handleSubmit((values)=> {
  console.log(values)
  alert("submitted!")
})
const {value: email} = useField<string>('email')
const {value: password} = useField<string>('password')

</script>
  