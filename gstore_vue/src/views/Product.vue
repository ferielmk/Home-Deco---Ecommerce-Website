<template>
        <div class="page-product">
            <div class="columns is-multiline">
                <div class="column is-9">
                    <figure class="image mb-6">
                        <img v-bind:src="product.get_image">
                    </figure>

                    <h1 class="title">{{ product.name }}</h1>
                  

                    <p>{{ product.description }}</p>
                    
                </div>

                <div class="column is-3">
                    <h2 class="subtitle">Information</h2>

                    <p><strong>Price: </strong>${{ product.price }}</p>

                    <div class="field has-addons mt-6">
                        <div class="control">
                            <input type="number" class="input" min="1" v-model="quantity">
                        </div>

                        <div class="control">
                            <a class="button is-dark" @click="addToCart">Add to cart</a>
                        </div>
                    </div>
                </div>

            </div>
        </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default{
    name: 'Product',
    data(){
        return{
            product: {},
            quantity: 1
            //price soldé
        }
    },
    mounted() {
        this.getProduct()
    },
    
    methods: {
        async getProduct() {
            //loading
            this.$store.commit('setIsLoading', true)

            //get the category slug from the url we are on
            const category_slug = this.$route.params.category_slug
            //get the product slug from the url we are on
            const product_slug = this.$route.params.product_slug

            //wait for axios to finish
            await axios   
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then( response => {
                    this.product = response.data

                    //set document title
                    document.title = this.product.name+ ' | Home Deco'
                })
                .catch(error => {
                    console.log(error)
                })
            //calculer solde pour ce produit, pour l'affichage
            //finished loading
            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            //check if the field quantity is a number or inf to 1
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            //ceate item with attributes product and quantity
            //this item is sent to the addTocart function in the store
            //so we can call these attributes for an item
            const item = {
                product: this.product,
                quantity: this.quantity
            }
            //call the store addToCart mutation
            this.$store.commit('addToCart', item)
            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        },
        
    }
}


</script>