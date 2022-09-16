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
import { useField } from 'vee-validate'
import BaseInput from '../components/BaseInput.vue'
import BaseButton from '../components/BaseButton.vue'


const onSubmit = () => {
  alert("submitted!")
}

const {value: email, errorMessage: emailError} = useField<string>('email', function(value) {
    if (!value) return 'This field is required'

    const regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    if (!regex.test(String(value).toLowerCase())) {
      return 'Please enter a valid email address'
    }
  
    return true
  })

const {value: password, errorMessage: passwordError} = useField<string>('password', function(value){
  if (!value) return 'This field is required'
  return true
})

</script>
  