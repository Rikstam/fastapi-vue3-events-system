<template>
<input type="radio"
        :checked="modelValue === value"
        :value="value"
        @change="$emit('update:modelValue', value)"
        v-bind="$attrs">
<label v-if="label">{{label}}</label>
</template>

<script setup lang="ts">
import {defineProps, withDefaults  } from 'vue'
interface Props {
    label?: string
    modelValue: string | number,
    value: string | number
}
const props = withDefaults(defineProps<Props>(), {
    label: '',
    modelValue: ''
})
</script>