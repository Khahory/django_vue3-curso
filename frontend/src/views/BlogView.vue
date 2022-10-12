<template>
  <div class="blog">
    <h1>This is BLOG</h1>
  </div>

  <br>
  <div v-for="post in APIData">
    <div>
      ID: {{ post.id }}<br>
      TITULO: {{ post.title }}<br>
      ESTADO: {{ post.status }}<br>

      <router-link :to="{name: 'blogPost', params: {id: post.id, title: post.title, slug: post.slug}}">
        SLUG: {{ post.slug }}<br>
      </router-link>
    </div>
    <br>
  </div>
</template>

<script>
import {getAPi} from "@/axios-api";

export default {
  name: 'Blog',
  data() {
    return {
      APIData: []
    }
  },
  created() {
    getAPi.get('blog/posts')
        .then(res => {
          console.log('tenemos info yeaaaa')
          this.APIData = res.data
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>
