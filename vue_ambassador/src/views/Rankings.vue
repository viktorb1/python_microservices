<template>
    <div class="table-responsive">
        <table class="table table-striped table-sm">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Revenue</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(value, name, i) in rankings" :key="i">
                    <td>{{ i + 1 }}</td>
                    <td>{{ name }}</td>
                    <td>{{ value }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue"
const rankings = ref([])

onMounted(async () => {
    const { data } = await axios.get("rankings")
    rankings.value = data
    console.log(data)
})

const checkoutUrl = (code: string) => `${import.meta.env.VITE_CHECKOUT_URL}/${code}`
</script>