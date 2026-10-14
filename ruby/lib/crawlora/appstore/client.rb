require "json"
require "net/http"
require "uri"

module Crawlora
  module Appstore
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"appstore-app": {"bodyParam": null, "bodyRequired": false, "id": "appstore-app", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"default": false, "description": "Include ratings histogram", "in": "query", "name": "ratings", "type": "boolean"}, {"default": false, "description": "Include the full device-platform compatibility list (adds one extra upstream fetch)", "in": "query", "name": "platforms", "type": "boolean"}], "path": "/appstore/app", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "ratings", "type": "boolean"}, {"in": "query", "name": "platforms", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "appstore-categories": {"bodyParam": null, "bodyRequired": false, "id": "appstore-categories", "method": "GET", "params": [], "path": "/appstore/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "appstore-collection": {"bodyParam": null, "bodyRequired": false, "id": "appstore-collection", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Room ID or EDS UUID collection ID from appstore_collections", "in": "query", "name": "collection_id", "required": true, "type": "string", "x-example": "6757461219"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/collection", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string"}, {"in": "query", "name": "collection_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-collections": {"bodyParam": null, "bodyRequired": false, "id": "appstore-collections", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/collections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-developer": {"bodyParam": null, "bodyRequired": false, "id": "appstore-developer", "method": "GET", "params": [{"description": "Developer artist ID", "in": "path", "name": "dev_id", "required": true, "type": "string", "x-example": "284882218"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/developer/{dev_id}", "pathParams": ["dev_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-editorial": {"bodyParam": null, "bodyRequired": false, "id": "appstore-editorial", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string", "x-example": "iphone"}, {"default": "main", "description": "Editorial section within the device", "enum": ["main", "arcade"], "in": "query", "name": "section", "type": "string"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/editorial", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string"}, {"enum": ["main", "arcade"], "in": "query", "name": "section", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-editorial-category": {"bodyParam": null, "bodyRequired": false, "id": "appstore-editorial-category", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Numeric App Store editorial page ID, discovered from appstore_editorial (same device)", "in": "query", "name": "category_id", "required": true, "type": "string", "x-example": "6503709728"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/editorial/category", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string"}, {"in": "query", "name": "category_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-list": {"bodyParam": null, "bodyRequired": false, "id": "appstore-list", "method": "GET", "params": [{"description": "Chart collection slug, see description for the full enum", "in": "query", "name": "collection", "type": "string", "x-example": "topfreeapplications"}, {"description": "Numeric App Store category ID, see description for the full enum; e.g. 6014 = Games, 7012 = Games/Puzzle", "in": "query", "name": "category", "type": "integer", "x-example": 6014}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"description": "Number of apps to return", "in": "query", "name": "num", "type": "integer", "x-example": 50}, {"default": false, "description": "Expand each app via lookup API", "in": "query", "name": "full_detail", "type": "boolean"}], "path": "/appstore/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "collection", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "full_detail", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "appstore-privacy": {"bodyParam": null, "bodyRequired": false, "id": "appstore-privacy", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "324684580"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/privacy/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-ratings": {"bodyParam": null, "bodyRequired": false, "id": "appstore-ratings", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/ratings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-reviews": {"bodyParam": null, "bodyRequired": false, "id": "appstore-reviews", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Review page number (1-10)", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"default": "mostRecent", "description": "Sort order", "enum": ["mostRecent", "mostHelpful"], "in": "query", "name": "sort", "type": "string"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["mostRecent", "mostHelpful"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-search": {"bodyParam": null, "bodyRequired": false, "id": "appstore-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "term", "required": true, "type": "string", "x-example": "panda"}, {"description": "Number of apps per page", "in": "query", "name": "num", "type": "integer", "x-example": 50}, {"description": "Search page number (1-based)", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"default": false, "description": "Return only app IDs", "in": "query", "name": "ids_only", "type": "boolean"}, {"default": "phone", "description": "App Store catalog to search: phone, pad, mac", "enum": ["phone", "pad", "mac"], "in": "query", "name": "platform", "type": "string"}], "path": "/appstore/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "term", "required": true, "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "ids_only", "type": "boolean"}, {"enum": ["phone", "pad", "mac"], "in": "query", "name": "platform", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-similar": {"bodyParam": null, "bodyRequired": false, "id": "appstore-similar", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/similar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-suggest": {"bodyParam": null, "bodyRequired": false, "id": "appstore-suggest", "method": "GET", "params": [{"description": "Partial search term", "in": "path", "name": "term", "required": true, "type": "string", "x-example": "panda"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}], "path": "/appstore/suggest/{term}", "pathParams": ["term"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-version-history": {"bodyParam": null, "bodyRequired": false, "id": "appstore-version-history", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "553834731"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/version-history/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["appstore-app", "appstore-categories", "appstore-collection", "appstore-collections", "appstore-developer", "appstore-editorial", "appstore-editorial-category", "appstore-list", "appstore-privacy", "appstore-ratings", "appstore-reviews", "appstore-search", "appstore-similar", "appstore-suggest", "appstore-version-history"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-appstore-ruby/0.1.2", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('app') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-app', params, response_type: response_type)
      end
      define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-categories', params, response_type: response_type)
      end
      define_method('collection') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-collection', params, response_type: response_type)
      end
      define_method('collections') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-collections', params, response_type: response_type)
      end
      define_method('developer') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-developer', params, response_type: response_type)
      end
      define_method('editorial') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-editorial', params, response_type: response_type)
      end
      define_method('editorial_category') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-editorial-category', params, response_type: response_type)
      end
      define_method('list') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-list', params, response_type: response_type)
      end
      define_method('privacy') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-privacy', params, response_type: response_type)
      end
      define_method('ratings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-ratings', params, response_type: response_type)
      end
      define_method('reviews') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-reviews', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-search', params, response_type: response_type)
      end
      define_method('similar') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-similar', params, response_type: response_type)
      end
      define_method('suggest') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-suggest', params, response_type: response_type)
      end
      define_method('version_history') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('appstore-version-history', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
