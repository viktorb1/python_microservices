<template>
    <div>
        <div class="pt-3 pb-2 mb-3 border-bottom">
            <v-btn href="/products/create" variant="contained" color="primary">Add</v-btn>
        </div>
        <v-table>
            <template v-slot:default>
                <thead>
                    <tr>
                        <th class="text-left">#</th>
                        <th class="text-left">Image</th>
                        <th class="text-left">Title</th>
                        <th class="text-left">Description</th>
                        <th class="text-left">Price</th>
                        <th class="text-left">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in products.slice((page - 1) * perPage, page * perPage)" :key="product.id">
                        <td>{{ product.id }}</td>
                        <td><v-img :src="product.image" max-height="80" max-width="120"></v-img></td>
                        <td>{{ product.title }}</td>
                        <td>{{ product.description }}</td>
                        <td>{{ product.price }}</td>
                        <td>
                            <v-btn-group>
                                <v-btn flat color="blue-darken-4" :href="`/products/${product.id}/edit`">Edit</v-btn>
                                <v-btn flat color="error" @click="del(product.id)">Delete</v-btn>
                            </v-btn-group>

                        </td>

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

interface Product {
    id: number,
    image: string,
    title: string,
    description: string,
    price: string,
}


const products = ref<Product[]>([])
const page = ref(1)
const perPage = ref(10)
const last_page = ref(0)

onMounted(async () => {
    const { data } = await axios.get("products", { withCredentials: true })
    products.value = data
    last_page.value = Math.ceil(data.length / perPage.value)
})

const del = async (id: number) => {
    if (confirm("Are you sure?")) {
        await axios.delete(`products/${id}`, { withCredentials: true })
        products.value = products.value.filter(p => p.id !== id)
    }
}
</script>


<style scoped></style>
