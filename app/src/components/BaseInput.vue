<template>
      <label :for="uuid">{{ label }}</label>
      <input
        v-bind="$attrs"
        class="field"
        :placeholder="label"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :id="uuid"
        :aria-describedby="error ? `${uuid}-error`: null"
        :aria-invalid="error ? true : null"
        >
        <p v-if="error"
           class="errorMessage"
           aria-live="assertive"
           :id="`${uuid}-error`"
           >
            {{error}}
        </p>
</template>
  
<script setup lang="ts">
  import { defineProps , withDefaults } from 'vue'
  import UniqueID from '../features/UniqueID'
  interface Props {
    label: string
    modelValue?:  string | number
    error?: string
  }
  const props = withDefaults(defineProps<Props>(),{
    error: '',
    value: ''
  })
  const uuid = UniqueID().getID().toString()
</script>
  
<style scoped>
  
</style>
  