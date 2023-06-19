<template>
    <Products :products="products" :filters="filters" @set-filters="filtersChanged" :lastPage="lastPage" />
</template>

<script setup lang="ts">
import Products from "@/views/Products.vue"
import { ref, onMounted, reactive } from "vue"
import axios from "axios"
import type { Product, Filter } from "types"


const products = ref<Product[]>([])
const filters = reactive<Filter>({
    s: "",
    sort: "",
    page: 1
})
const lastPage = ref(0)


const filtersChanged = async (f: Filter) => {
    filters.s = f.s
    filters.sort = f.sort
    filters.page = f.page

    const arr = []

    if (filters.s) {
        arr.push(`s=${filters.s}`)
    }

    if (filters.sort) {
        arr.push(`sort=${filters.sort}`)
    }

    if (filters.page) {
        arr.push(`page=${filters.page}`)
    }

    const { data } = await axios.get(`products/backend?${arr.join('&')}`)

    if (filters.page == 1) {
        products.value = data.data
    } else {
        products.value = [...products.value, ...data.data]
    }
    console.log(`products/backend?${arr.join('&')}`)

    lastPage.value = data.meta.last_page
}

onMounted(() => filtersChanged(filters))

</script>