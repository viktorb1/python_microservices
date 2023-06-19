<template>
    <div class="table-responsive">
        <table class="table table-striped table-sm">
            <thead>
                <tr>
                    <th>Link</th>
                    <th>Users</th>
                    <th>Revenue</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="link in links" :key="link.id">
                    <td>{{ checkoutUrl(link.code) }}</td>
                    <td>{{ link.count }}</td>
                    <td>{{ link.revenue }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue"
const links = ref([])

onMounted(async () => {
    const { data } = await axios.get("stats")
    links.value = data
})

const checkoutUrl = (code: string) => `${import.meta.env.VITE_CHECKOUT_URL}/${code}`
</script>