<template>
    <div>
        <v-table>
            <template v-slot:default>
                <thead>
                    <tr>
                        <th class="text-left">#</th>
                        <th class="text-left">Name</th>
                        <th class="text-left">Email</th>
                        <th class="text-left">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in users.slice((page - 1) * perPage, page * perPage)" :key="user.id">
                        <td>{{ user.id }}</td>
                        <td>{{ user.first_name }} {{ user.last_name }}</td>
                        <td>{{ user.email }}</td>
                        <td><v-btn :href="`/users/${user.id}/links`" color="primary">
                                View
                            </v-btn></td>
                    </tr>
                </tbody>
            </template>
        </v-table>

        <v-pagination v-model="page" total-visible="7" :length="last_page"></v-pagination>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue"
import axios from "axios"

interface User {
    id: number;
    first_name: string;
    last_name: string;
    email: string;
    is_ambassador: boolean;
}


const users = ref<User[]>([])
const page = ref(1)
const perPage = ref(10)
const last_page = ref(0)

onMounted(async () => {
    const { data } = await axios.get("ambassadors", { withCredentials: true })
    users.value = data
    last_page.value = Math.ceil(data.length / perPage.value)
})
</script>
