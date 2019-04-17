#------------------------------------------------------------------------------
# HTMLExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------

## Exports a basic HTML document.  This exporter assists with the export of HTML.
#  Inherit from it if you are writing your own HTML template and need custom
#  preprocessors/filters.  If you don't need custom preprocessors/ filters, just
#  change the 'template_file' config option.

## The text used as the text for anchor links. Set to empty since we'll use anchor.js for the links
c.HTMLExporter.anchor_link_text = " "

# Extract output images to files
c.ExtractOutputPreprocessor.enabled = True
