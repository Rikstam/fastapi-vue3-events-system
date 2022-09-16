<template>
<input
    :id="uuid"
    type="checkbox"
    :checked="modelValue"
    @change="$emit('update:modelValue', $event.target.checked)"
    class="field"
>
<label :for="uuid">{{label}}</label>
<p v-if="error"
           class="errorMessage"
           aria-live="assertive"
           :id="`${uuid}-error`"
           >
            {{error}}
        </p>
</template>

<script setup lang="ts">
import {defineProps, withDefaults  } from 'vue'
import UniqueID from '../features/UniqueID';
interface Props {
    label: string
    modelValue:  boolean
    error?: string
}
const props = withDefaults(defineProps<Props>(), {
    modelValue: false,
    error: ''
})

const uuid = UniqueID().getID().toString()

</script>