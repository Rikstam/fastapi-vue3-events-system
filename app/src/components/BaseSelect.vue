<template>
<label>{{label}}</label>
      <select
        :value="modelValue"
        class="field"
        v-bind="{
            ...$attrs,
            onChange:($event) => { $emit('update:modelValue', $event.target.value)}
            }">
        <option
          v-for="option in options"
          :value="option"
          :key="option"
          :selected="option === modelValue"
        >
          {{ option }}
        </option>
      </select>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
interface Props {
    label: string
    modelValue: string | number
    options: string[]
}
const props = defineProps<Props>()
</script>