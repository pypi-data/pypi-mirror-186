depends = ('ITKPyBase', 'ITKIOImageBase', 'ITKIOHDF5', )
templates = (  ('OMEZarrNGFFImageIO', 'itk::OMEZarrNGFFImageIO', 'itkOMEZarrNGFFImageIO', True),
  ('OMEZarrNGFFImageIOFactory', 'itk::OMEZarrNGFFImageIOFactory', 'itkOMEZarrNGFFImageIOFactory', True),
)
factories = (("ImageIO","OMEZarrNGFF"),)
