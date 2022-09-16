<template>
<label :for="uuid">{{label}}</label>
      <select
        :value="modelValue"
        class="field"
        :id="uuid"
        :error="error"
        :aria-describedby="error ? `${uuid}-error`: null"
        :aria-invalid="error ? true : null"
        v-bind="{
            ...$attrs,
            onChange:($event) => { $emit('update:modelValue', $event.target.value)}
            }"
            >
        <option
          v-for="option in options"
          :value="option"
          :key="option"
          :selected="option === modelValue"
        >
          {{ option }}
        </option>
      </select>
      <p v-if="error"
           class="errorMessage"
           aria-live="assertive"
           :id="`${uuid}-error`"
           >
            {{error}}
        </p>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
import UniqueID from '../features/UniqueID'
interface Props {
    label: string
    modelValue?: string | number
    options: string[]
    error?: string
}
const props = defineProps<Props>()
const uuid = UniqueID().getID().toString()
</script>