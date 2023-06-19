<template>
    <div class="col-md-12 mb-4" v-if="link">
        <div class="alert alert-info" role="alert">
            {{ link }}
        </div>
    </div>
    <div class="col-md-12 mb-4" v-if="error">
        <div class="alert alert-danger" role="alert">
            {{ error }}
        </div>
    </div>

    <div class="col-md-12 mb-4 input-group">
        <input class="form-control" placeholder="Search" @keyup="search(($event.target as HTMLInputElement).value)" />
        <div class="input-group-append" v-if="selected.length > 0">
            <button class="btn btn-info" @click="generate">Generate Link</button>
        </div>

        <div class="input-group-append">
            <select class="form-select" @change="sort(($event.target as HTMLInputElement).value)">
                <option>Select</option>
                <option value="asc">Price Ascending</option>
                <option value="desc">Price Descending</option>
            </select>
        </div>
    </div>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="product in products" :key="product.id" @click="select(product.id)">
            <div :class="selected.includes(product.id) ? 'card shadow-sm selected' : 'card shadow-sm'">
                <img :src="product.image" height="200" />
                <div class="card-body">
                    <p class="card-text">{{ product.title }}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <small class="text-body-secondary">${{ product.price }}</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="d-flex justify-content-center mt-4" v-if="filters.page < lastPage">
        <button class="btn btn-primary" @click="loadMore">Load More</button>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import type { Filter, Product } from 'types';
import { ref } from "vue"

const selected = ref<number[]>([])
const link = ref("")
const error = ref("")


const props = defineProps<{
    products: Product[];
    filters: Filter;
    lastPage: number;
}>()

const emit = defineEmits(['set-filters'])

const search = (s: string) => {
    emit('set-filters', {
        ...props.filters,
        s,
        page: 1
    })
}

const sort = (sort: string) => {
    emit('set-filters', {
        ...props.filters,
        sort,
        page: 1
    })
}

const loadMore = () => {
    emit('set-filters', {
        ...props.filters,
        page: props.filters.page + 1
    })
}

const select = (id: number) => {
    if (selected.value.includes(id)) {
        selected.value = selected.value.filter(item => item !== id);
    } else {
        selected.value = [...selected.value, id]
    }
}

const generate = async () => {
    try {
        const { data } = await axios.post("links", {
            products: selected.value
        })
        link.value = `Link generated: ${import.meta.env.VITE_CHECKOUT_URL}/${data.code}`

    } catch (e) {
        error.value = "You should be logged in to generate a link."
    } finally {
        setTimeout(() => {
            link.value = ""
            error.value = ""
        }, 5000)
    }
}

</script>


<style scoped>
.card {
    cursor: pointer
}

.card.selected {
    border: 4px solid darkcyan;
}
</style>