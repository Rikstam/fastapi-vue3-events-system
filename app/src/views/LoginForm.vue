<template>
    <form @submit.prevent="onSubmit">
      <BaseInput
        label="Email"
        type="email"
        v-model="email"
        :error="emailError"
      />
  
      <BaseInput
        label="Password"
        type="password"
        v-model="password"
        :error="passwordError"
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

const validations = {
  email: (value: string) => {
    if (!value) return 'This field is required'

    const regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    if (!regex.test(String(value).toLowerCase())) {
      return 'Please enter a valid email address'
    }
  
    return true
  },
  password: (value: string) => {
    const requiredMessage = 'Password is required'
    if (value === undefined ||  value === null) return requiredMessage
    if(!String(value).length) return requiredMessage
    return true
  }
}

const onSubmit = () => {
  alert("submitted!")
}

useForm({
  validationSchema: validations
})

const {value: email, errorMessage: emailError} = useField<string>('email')

const {value: password, errorMessage: passwordError} = useField<string>('password')

</script>
  