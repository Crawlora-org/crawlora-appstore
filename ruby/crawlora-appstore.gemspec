require_relative "lib/crawlora/appstore/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-appstore"
  spec.version = Crawlora::Appstore::VERSION
  spec.summary = "App Store API client for Crawlora (15 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted App Store API. Covers app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers across 15 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-appstore", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-appstore/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
