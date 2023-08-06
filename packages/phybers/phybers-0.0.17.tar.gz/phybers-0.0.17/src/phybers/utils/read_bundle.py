import os
import numpy as N

def read_bundle( infile ):
  """ Read Bundles File.
  """
  points = []
  bun_file = infile + 'data'
  os.path.getsize( bun_file )
  bytes = os.path.getsize( bun_file )
  num = bytes / 4

  num_count = 0
  f = open( bun_file , 'rb')
  while num_count < num:
    p = N.frombuffer( f.read( 4 ), dtype=N.int32 )[ 0 ] # numero de puntos de la fibra
    vertex = N.frombuffer( f.read( p * 3 * 4 ), dtype=N.float32 ).reshape( -1, 3 ) # lee coordenadas fibra
    points.append( vertex )
    num_count = num_count + 1 + ( p * 3 )

  f.close()

  return points
