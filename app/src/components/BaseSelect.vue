<template>
<label :for="uuid">{{label}}</label>
      <select
        :value="modelValue"
        class="field"
        :id="uuid"
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
import UniqueID from '../features/UniqueID'
interface Props {
    label: string
    modelValue: string | number
    options: string[]
}
const props = defineProps<Props>()
const uuid = UniqueID().getID().toString()
</script>