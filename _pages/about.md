---
layout: about
title: About
permalink: /
# subtitle: Indie game dev based in the Potteries.

profile:
  align: right
  image: profile-pictures/domdfcoding.jpeg
  image_circular: false # crops the image to make it circular
  more_info: >
    <div class="pb-3 text-center">
        <p class="m-0"><a href="https://github.com/domdfcoding">domdfcoding</p>
        <p class="m-0"><i class="fa-solid fa-location-dot"></i><span class="pl-1">Stoke on Trent, UK</span>
        </p>
    </div>

social: true # includes social icons at the bottom of the page

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

Forensic gunshot residue researcher turned software developer and purveyor of Christmas ornaments and electronic kits.


<div class="row row-cols-2">
  <div class="col mb-4">
    <a href="/research">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/cartridge_cases_thumbnail.JPG" sizes = "250px" alt="Cartridge Cases" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title no-anchor">Research</h3>
          <p class="card-text">My organic gunshot residue research.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col mb-4">
    <a href="/repositories">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/org_grid.png" sizes = "250px" alt="Open Source Software" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title  no-anchor">Repositories</h3>
          <p class="card-text">My open source software projects.</p>
        </div>
      </div>
    </a>
  </div>

  <div class="col mb-4">
    <a href="/videos">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/video_thumbnail.png" sizes = "250px" alt="Videos" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title  no-anchor">Videos</h3>
          <p class="card-text">My YouTube videos.</p>
        </div>
      </div>
    </a>
  </div>
  <div class="col mb-4">
    <a href="https://potbanksoftware.github.io">
      <div class="card h-100 hoverable">
        {% include figure.liquid loading="eager" path="/assets/img/potbank-software-logo.png" sizes = "250px" alt="Potbank Software Logo" class="card-img-top" %}
        <div class="card-body">
          <h3 class="card-title  no-anchor">Potbank Software</h3>
          <p class="card-text">
            My indie game developer.
          </p>
        </div>
      </div>
    </a>
  </div>
</div>
