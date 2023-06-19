<template>
    <Products :products="filteredProducts" :filters="filters" @set-filters="filtersChanged" :lastPage="lastPage" />
</template>

<script setup lang="ts">
import Products from "@/views/Products.vue"
import { ref, onMounted, reactive } from "vue"
import axios from "axios"
import type { Product, Filter } from "types"


const products = ref<Product[]>([])
const filteredProducts = ref()
const filters = reactive<Filter>({
    s: "",
    sort: "",
    page: 1
})

const perPage = 9
const lastPage = ref(0)


const filtersChanged = (f: Filter) => {
    filters.s = f.s
    filters.sort = f.sort
    filters.page = f.page

    filteredProducts.value = products.value.filter(p => p.title.toLowerCase().indexOf(filters.s.toLowerCase()) >= 0 || p.description.toLowerCase().indexOf(filters.s.toLowerCase()) >= 0)

    if (filters.sort === "asc" || filters.sort === "desc") {
        filteredProducts.value.sort((a: Product, b: Product) => {
            const diff = a.price - b.price;
            if (diff === 0) return 0
            const sign = Math.abs(diff) / diff
            return filters.sort === 'asc' ? sign : -sign
        })
    }

    lastPage.value = Math.ceil(filteredProducts.value.length / perPage)
    filteredProducts.value = filteredProducts.value.slice(0, filters.page * perPage)
}

onMounted(async () => {
    const { data } = await axios.get("products/frontend")
    products.value = data
    filteredProducts.value = data.slice(0, filters.page * perPage)
    lastPage.value = Math.ceil(data.length / perPage)
})
</script>