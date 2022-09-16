<template>
<input
    :id="uuid"
    type="checkbox"
    :checked="modelValue"
    @change="$emit('update:modelValue', $event.target.checked)"
    class="field"
>
<label :for="uuid">{{label}}</label>
</template>

<script setup lang="ts">
import {defineProps, withDefaults  } from 'vue'
import UniqueID from '../features/UniqueID';
interface Props {
    label: string
    modelValue:  boolean
}
const props = withDefaults(defineProps<Props>(), {
    modelValue: false
})

const uuid = UniqueID().getID().toString()

</script>