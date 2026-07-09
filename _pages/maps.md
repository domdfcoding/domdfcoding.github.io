---
layout: page
permalink: /maps/
title: Maps
description: Various maps and related utilities I've made with leaflet and OpenStreetMap
nav: true
nav_order: 6
---

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.map_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>

<div class="maps d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center align-items-md-stretch" style="gap: 10px">

  {% for map in site.data.repositories.maps %}
    {% include map_card.liquid map=map %}
  {% endfor %}

</div>
