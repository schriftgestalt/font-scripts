#MenuTitle: Update metrics in unique glyphs
# -*- coding: utf-8 -*-

__doc__="""
Updates horizontal metrics in unique glyphs only. Re-interpolates sidebearings of all intermediate masters. Unique, in this script, means the glyph catgory is not "Separator," the glyph name does not end with "comb" or ".tf", and the glyph is not made up of only auto-aligned components.
"""

font = Glyphs.font
uniques = []

for glyph in font.glyphs:
	if(glyph.glyphInfo):
		autoAligned = False
		autoAlignedComponents = 0
		componentCount = 0
		for layer in glyph.layers:
			if layer.isMasterLayer:
				for component in layer.components:
					componentCount += 1
					if component.automaticAlignment is True:
						autoAlignedComponents += 1
		if(componentCount > 0 and componentCount == autoAlignedComponents):
			autoAligned = True
		if glyph.glyphInfo.category != "Separator" and not name.endswith("comb") and not name.endswith(".tf") and autoAligned is False and glyph.export == True:
			print("Updating %s" % glyph.name)
			uniques.append(glyph)

# re-interpolate sidebearings on all special layers
for glyph in font.glyphs:
	for layer in glyph.layers:
		if layer.isSpecialLayer:
			layer.reinterpolateMetrics()
			layer.syncMetrics()
# sync metrics on all uniques
for glyph in uniques:
	for layer in glyph.layers:
		layer.syncMetrics()