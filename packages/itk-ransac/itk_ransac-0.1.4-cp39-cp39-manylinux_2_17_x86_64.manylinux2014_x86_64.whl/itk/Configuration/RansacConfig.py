depends = ('ITKPyBase', 'ITKRegistrationMethodsv4', 'ITKRegistrationCommon', 'ITKOptimizersv4', 'ITKOptimizers', 'ITKMetricsv4', 'ITKMesh', 'ITKIOMeshBase', 'ITKCommon', )
templates = (  ('ParametersEstimator', 'itk::ParametersEstimator', 'itkParametersEstimatorPD6', True, 'itk::Point< double, 6>, double'),
  ('LandmarkRegistrationEstimator', 'itk::LandmarkRegistrationEstimator', 'itkLandmarkRegistrationEstimatorD6S', True, '6, itk::Similarity3DTransform <double>'),
  ('LandmarkRegistrationEstimator', 'itk::LandmarkRegistrationEstimator', 'itkLandmarkRegistrationEstimatorD6V', True, '6, itk::VersorRigid3DTransform <double>'),
  ('RANSAC', 'itk::RANSAC', 'itkRANSACPD6S', True, 'itk::Point< double, 6>, double, itk::Similarity3DTransform <double>'),
  ('RANSAC', 'itk::RANSAC', 'itkRANSACPD6V', True, 'itk::Point< double, 6>, double, itk::VersorRigid3DTransform <double>'),
)
factories = ()
