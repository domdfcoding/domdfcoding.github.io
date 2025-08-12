source "https://rubygems.org"

gem "jekyll", "~> 4.4"

# Core plugins that directly affect site building
group :jekyll_plugins do
    gem "jekyll-archives-v2"
    gem "jekyll-sitemap", "~> 1.4"
    gem "jekyll-paginate-v2"
    gem "jekyll-email-protect"
    gem "jekyll-feed", "~> 0.17.0"
    gem "jemoji", "~> 0.13.0"
    gem "jekyll-get-json"
    gem "jekyll-imagemagick"
    gem "jekyll-link-attributes"
    gem "jekyll-minifier"
    gem "jekyll-regex-replace"
    gem "jekyll-tabs"
    gem "jekyll-terser", :git => "https://github.com/RobertoJBeltran/jekyll-terser.git"
    gem "jekyll-toc"
    gem "jekyll-sass-converter", "~> 3.1.0"
    gem "jekyll-og-image", :git => "https://github.com/potbanksoftware/jekyll-og-image", :branch => "flatten-inset-image"

    gem 'classifier-reborn'  # used for content categorization during the build
end

# Gems for development or external data fetching (outside :jekyll_plugins)
group :other_plugins do
    gem 'css_parser'
    gem 'feedjira'
    gem 'httparty'
    # gem 'terser'         # used by jekyll-terser
    # gem 'unicode_utils' -- should be already installed by jekyll
    # gem 'webrick' -- should be already installed by jekyll
end
