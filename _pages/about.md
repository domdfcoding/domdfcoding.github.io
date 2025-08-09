---
layout: about
title: about
permalink: /
subtitle: Indie game dev based in the Potteries.

profile:
  align: right
  image: logo.svg
  image_circular: false # crops the image to make it circular
  more_info: >
    <div class="pb-3 text-center">
        <p class="m-0"><small>Owned by Dominic Davis-Foster</small></p>
        <p class="m-0">Made in<br><i class="fa-solid fa-location-dot"></i><span class="pl-1">Stoke on Trent, UK</span>
        </p>
    </div>

social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<style>
  header.post-header {
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 20px
    }
  .card figure  { margin-bottom: 0.2rem;}
  .card .card-body  { padding-top: 0;}
  .image-credit, .image-credit span a {font-size: 8pt;}
</style>

Potbank Software is a one man indie game developer in Stoke on Trent, UK.


<div class="row row-cols-2">
  <div class="col mb-4">
    <a href="/games">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/cabal_chemist_screenshot.png" sizes = "250px" alt="Games" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title">Games</h3>
          <p class="card-text">Games developed by Potbank Software.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col mb-4">
    <a href="/fallout-mods">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/sam-clarke-ZEfFgaXVaV4-unsplash.jpg" sizes = "250px" alt="Games" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title">Fallout Mods</h3>
          <p class="card-text">Mods and tools for Fallout 3 and New Vegas.</p>
        </div>
        <div class="image-credit mt-auto mx-auto">
          <a></a>
          Photo by <a href="https://unsplash.com/@clarke_designs_photography">Sam Clarke</a> on <a href="https://unsplash.com/photos/red-and-black-cordless-power-drill-beside-black-and-red-cordless-power-drill-ZEfFgaXVaV4">Unsplash</a>
        </div>
      </div>
    </a>
  </div>

  <div class="col mb-4">
    <a href="/godot-tools">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/godot_logo.png" sizes = "250px" alt="Godot Addons" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title">Godot Addons</h3>
          <p class="card-text">Addons/plugins for Godot and associated tools.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col mb-4">
    <a href="/blog">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/florian-klauer-mk7D-4UCfmg-unsplash.jpg" sizes = "250px" alt="Blog" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title">Blog</h3>
          <p class="card-text">
            Development blog.
          </p>
        </div>
        <div class="image-credit mt-auto mx-auto">
          <a></a>
          Photo by <a href="https://unsplash.com/@florianklauer">Florian Klauer</a> on <a href="https://unsplash.com/photos/black-fayorit-typewriter-with-printer-paper-mk7D-4UCfmg">Unsplash</a>
        </div>
      </div>
    </a>
  </div>
</div>
  

## The Logo

Potbank Software's logo is a [Bottle Oven](https://en.wikipedia.org/wiki/Bottle_oven), once widely used in the Potteries around Stoke on Trent for firing ceramics.
