<template>
    <component 
    v-for="option in options"
    :key="option.value"
    :is="vertical ? 'div': 'span'"
    :class="{horizontal: !vertical}">
    <BaseRadio
        :label="option.label"
        :value="option.value"
        :name="name"
        :modelValue="modelValue"
        @update:modelValue="$emit('update:modelValue', $event)"
        :error="error"
    />
</component>
</template>
<script setup lang="ts">
import { defineProps, withDefaults } from 'vue'
import BaseRadio from './BaseRadio.vue';
interface Props {
    options: {
        label:string
        value: string | number
    }[],
    name: string,
    modelValue: string | number,
    vertical: boolean
    error?: string
}
const props = withDefaults(defineProps<Props>(),{
    vertical: false,
    error: ''
})
</script>

<style scoped>
    .horizontal {
        margin-right: 20px;
    }
</style>