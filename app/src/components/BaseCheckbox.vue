<template>
<input
    type="checkbox"
    :checked="modelValue"
    @change="$emit('update:modelValue', $event.target.checked)"
    class="field"
>
<label>{{label}}</label>
</template>

<script setup lang="ts">
import {defineProps, withDefaults  } from 'vue'
interface Props {
    label: string
    modelValue:  boolean
}
const props = withDefaults(defineProps<Props>(), {
    modelValue: false
})
</script>