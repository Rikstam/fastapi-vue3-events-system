<template>
      <label>{{ label }}</label>
      <input
        v-bind="$attrs"
        class="field"
        :placeholder="label"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        >
</template>
  
<script setup lang="ts">
  import { defineProps } from 'vue'
  interface Props {
    label: string
    modelValue:  string | number
  }
  const props = defineProps<Props>()
</script>
  
<style scoped>
  
</style>
  