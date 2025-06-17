module Jekyll
  class IncludeCodeTag < Liquid::Tag
    SYNTAX = /file="(?<file>[^"]+)"(?:\s+title="(?<title>[^"]*)")?(?:\s+lines="(?<lines>\d+-\d+)")?(?:\s+show_filename=(?<show_filename>true|false))?/

    def initialize(tag_name, markup, tokens)
      super
      if markup.strip =~ SYNTAX
        @file = Regexp.last_match[:file]
        @title = Regexp.last_match[:title]
        @lines = Regexp.last_match[:lines]
        @show_filename = Regexp.last_match[:show_filename] != "false"
      else
        raise SyntaxError, "Invalid syntax for include_code. Expected: file=\"filename.py\" [title=\"...\"] [lines=\"X-Y\"] [show_filename=true|false]"
      end
    end

    def render(context)
      site_source = context.registers[:site].source
      code_path = File.join(site_source, "_includes", "code", @file)

      raise IOError, "File #{code_path} not found" unless File.exist?(code_path)

      code = File.readlines(code_path)
      if @lines
        first, last = @lines.split('-').map(&:to_i)
        code = code[(first - 1)..(last - 1)]
      end

      output = []
      output << "<figure class=\"code\">"

      if @title || @show_filename
        caption = []
        caption << @title if @title
        caption << @file if @show_filename
        output << "<figcaption>#{caption.join(' — ')}</figcaption>"
      end

      output << "```python"
      output << code.map(&:rstrip).join("\n")
      output << "```"

      output.join("\n")
    end
  end
end

Liquid::Template.register_tag('include_code', Jekyll::IncludeCodeTag)
