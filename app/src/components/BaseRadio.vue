<template>
<input type="radio"
        :id="uuid"
        :checked="modelValue === value"
        :value="value"
        @change="$emit('update:modelValue', value)"
        v-bind="$attrs">
<label v-if="label" :for="uuid">{{label}}</label>
</template>

<script setup lang="ts">
import {defineProps, withDefaults  } from 'vue'
import UniqueID from '../features/UniqueID';
interface Props {
    label?: string
    modelValue: string | number,
    value: string | number
}
const props = withDefaults(defineProps<Props>(), {
    label: '',
    modelValue: ''
})

const uuid = UniqueID().getID().toString()

</script>