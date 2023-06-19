export interface Product {
  id: number
  title: string
  description: string
  image: string
  price: number
}

export interface Filter {
  s: string
  sort: string
  page: number
}
